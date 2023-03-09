import axios from 'axios'


//Axios instance for use elesewhere in React
const axiosInstance = axios.create({
	baseURL: 'http://127.0.0.1:8000/api/',
	timeout: 5000,
    //The header must contain JWT(a space)+access_token for authorization, this is retrieved from localstorage
	headers: {
		Authorization: localStorage.getItem('access_token')
            ? 'JWT ' + localStorage.getItem('access_token')
            : null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	},
});


axiosInstance.interceptors.response.use(
	(response) => {
		return response;
	},
	async function (error) {
		const originalRequest = error.config;


		//if token not valid
		if (error.response.data.code === 'token_not_valid' && error.response.status === 401 && error.response.statusText === 'Unauthorized') {	
			//Check refresh token is still valid
			const refreshToken = localStorage.getItem('refresh_token');

			if (refreshToken) {
				const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));
				
				//get current time in seconds
				const currentTime = Math.ceil(Date.now() / 1000);

				//if refresh still valid, update access and refresh
				if (tokenParts.exp > currentTime) {
					return axiosInstance
						.post('/token/refresh/', {
							refresh: refreshToken
						})
						.then((response) => {
							localStorage.setItem('access_token', response.data.access);
							localStorage.setItem('refresh_token', response.data.refresh);

							axiosInstance.defaults.headers['Authorization'] = 'JWT ' + response.data.access;
							originalRequest.headers['Authorization'] = 'JWT ' + response.data.access;

							return axiosInstance(originalRequest);
						});
				} 
			}
		}
		//token invalid
		return Promise.reject(error);
	}
);


export default axiosInstance;