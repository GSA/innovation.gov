---
# This front matter is required for https://github.com/babel/jekyll-babel
---

/**
 * fetchGoogleSheet - Fetch a Google spreadsheet's worksheet and store it in
 * session storage that subsequent requests don't require an AJAX request. Session
 * storage is cleared whenever the user closes their browser or opens the website
 * in a new browser tab/window.
 *
 * @param {string} spreadsheet Spreadsheet's ID
 * @param {string} worksheet Worksheet's ID
 *
 * @return {type} Description
 */
const fetchGoogleSheet = ({ spreadsheet, worksheet }) => {

  const url = `https://spreadsheets.google.com/feeds/list/${spreadsheet}/${worksheet}/public/values?alt=json`;

  const supportsSessionStorage = 'sessionStorage' in window;

  // Request JSON using jQuery's getJSON
  const getJSON = url => {
    const promise = $.getJSON(url);
    promise.done(data => sessionStorage.setItem(url, JSON.stringify(data)));
    return promise;
  }

  // Get the JSON from session storage. If it's not there, fallback to getJSON.
  const getStorage = url => {
    const storageDfd = new $.Deferred();
    const storedData = sessionStorage.getItem(url);
    if (!storedData) {
      return getJSON(url);
    }
    setTimeout(() => storageDfd.resolveWith(null, [JSON.parse(storedData)]));
    return storageDfd.promise();
  }

  // If the user's browser supports session storage, use it. Otherwise, fallback
  // to jQuery's getJSON.
  return supportsSessionStorage ? getStorage(url) : getJSON(url);

};
