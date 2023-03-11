import axios from "axios";

//Axios instance for use elesewhere in React
const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 50000,
  //The header must contain JWT(a space)+access_token for authorization, this is retrieved from localstorage
  headers: {
    Authorization: localStorage.getItem("access_token")
      ? "JWT " + localStorage.getItem("access_token")
      : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error.config;

    //token invalid
    return Promise.reject(error);
  }
);
export default axiosInstance;
