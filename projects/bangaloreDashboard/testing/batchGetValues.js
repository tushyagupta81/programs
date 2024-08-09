require("coffee-script/register");
var gapi = require("gapi");

function batchGetValues(spreadsheetId, callback) {
  let ranges = [
    // Range names ...
  ];
  // ranges = _ranges;
  try {
    gapi.client.sheets.spreadsheets.values
      .batchGet({
        spreadsheetId: spreadsheetId,
        // ranges: ranges,
      })
      .then((response) => {
        const result = response.result;
        console.log(`${result.valueRanges.length} ranges retrieved.`);
        if (callback) callback(response);
      });
  } catch (err) {
    // document.getElementById("content").innerText = err.message;
    console.log(err);
    return;
  }
}

const spreadsheetId = "1eiAlAzkhvOV7pTbCb9EGR_1Ijmz00_up4JO-XD7nWiA";

function onClickHandle() {
  batchGetValues(spreadsheetId, (response) => {
    console.log(response.sheetsByIndex[0].title); // Log the retrieved values
  });
}

document
  .getElementById("batch")
  .addEventListener("onclick", () => onClickHandle());
