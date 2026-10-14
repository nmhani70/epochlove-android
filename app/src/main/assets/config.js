// ===== SERVER CONFIGURATION =====
// Update this URL to your VPS domain (after you set it up).
var SERVER_URL = "https://example.com";
var WS_URL = "wss://example.com/ws";

var IS_APP_MODE = (location.protocol === "file:");

function getApiUrl(path) {
  if (IS_APP_MODE) return SERVER_URL + path;
  return path;
}

function getWsUrl() {
  if (IS_APP_MODE) return WS_URL;
  var proto = location.protocol === "https:" ? "wss" : "ws";
  return proto + "://" + location.host + "/ws";
}
