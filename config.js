// Dual Track settings. Edit this file on GitHub, then commit.
window.DUAL_TRACK_CONFIG = {

  // 1) Firebase settings for student and admin accounts.
  //    Firebase console > Project settings > Your apps > Web app > "SDK setup and configuration" > Config.
  //    Paste the object between the braces below.
  //    Leave this as null to run without accounts (progress saved only in each browser).
  firebase: null,
  // firebase: {
  //   apiKey: "PASTE",
  //   authDomain: "PASTE",
  //   projectId: "PASTE",
  //   storageBucket: "PASTE",
  //   messagingSenderId: "PASTE",
  //   appId: "PASTE"
  // },

  // 2) Admin email addresses, in lowercase. Must also be listed in firestore.rules.
  adminEmails: ["your-email@example.com"],

  // 3) Optional. Video links if you are NOT using accounts (with accounts, add them on the Admin page).
  //    Example: { 1: "https://youtu.be/xxxxxxxxxxx", 2: "https://youtu.be/yyyyyyyyyyy" }
  videoLinks: {}
};
