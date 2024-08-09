const GSheetReader = require("g-sheets-api");
const options = {
  apiKey: "AIzaSyA1XwCaJkCIDVEckQDFEnWi82vXQhkBGJo",
  sheetId: "1eiAlAzkhvOV7pTbCb9EGR_1Ijmz00_up4JO-XD7nWiA",
};
GSheetReader(options, (results) => {
  console.log(results);
}).catch((err) => {
  console.log(err);
});
