// Dual Track settings. Edit this file on GitHub, then commit.
window.DUAL_TRACK_CONFIG = {

  // 1) Accounts: your Supabase (PostgreSQL) project.
  //    Supabase dashboard > Project Settings > API: copy the Project URL and the "anon public" key.
  //    The anon key is meant to be public. The rules in supabase/setup.sql protect the data.
  //    Leave this as null to run without accounts (progress saved only in each browser).
  supabase: null,
  // supabase: {
  //   url: "https://YOUR-PROJECT.supabase.co",
  //   anonKey: "PASTE"
  // },

  // 2) Admins are set in the database: the ADMIN EMAIL line in supabase/setup.sql.

  // 3) Optional. Video links if you are NOT using accounts (with accounts, add them on the Admin page).
  //    Example: { 1: "https://youtu.be/xxxxxxxxxxx", 2: "https://youtu.be/yyyyyyyyyyy" }
  videoLinks: {}
};
