import axios from "axios";

import { FOODTRUCK_SERVER_API } from "@env";

const axiosInit = axios.create({
  baseURL: `${FOODTRUCK_SERVER_API}/foodtrucks/`,
  responseType: "json",
});

export const getAllFoodtrucks = (headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit
          .get("", headers)
          .then((res) => resolve(res.data))
          .catch((err) => reject(err.response.data));
      } catch (err) {
        reject("System error. Please try again later.");
      }
    }, 1000)
  );

export const getFoodtruck = (slug, headers) =>
  new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        axiosInit
          .get(`${slug}`, headers)
          .then((res) => resolve(res.data))
          .catch((err) => reject(err.response.data));
      } catch (err) {
        reject("System error. Please try again later.");
      }
    }, 1000)
  );