import axios from 'axios'

/**
 * A services bridge to out-side services.
 */
export default class HttpClient {
  /**
   * {HttpClient} constructor
   * @param {String} baseUrl - API base Url.
   */
  constructor (baseUrl) {
    this.client = axios.create({ baseURL: baseUrl })
  }

  /**
   * Sends a get request.
   * @param {String} path - path to the request to be joined with the API base url.
   * @param {Function} successCallback - function on success.
   * @param {Function} errorCallback - function on error.
   * @param {Function} finallyCallback - function to be called always.
   * @private
   */
  get (path, successCallback, errorCallback, finallyCallback) {
    this.client.get(UrlHelper.normalizePath(path))
        .then(successCallback)
        .catch(errorCallback)
        .then(finallyCallback)
  }

  /**
   * Sends a post request.
   * @param {String} path - path to the request to be joined with the API base url.
   * @param {Object} data - data to be posted.
   * @param {Function} successCallback - function on success.
   * @param {Function} errorCallback - function on error.
   * @param {Function} finallyCallback - function to be called always.
   */
  post (path, data, successCallback, errorCallback, finallyCallback) {
    this.client.post(UrlHelper.normalizePath(path), data)
        .then(successCallback)
        .catch(errorCallback)
        .then(finallyCallback)
  }
}
