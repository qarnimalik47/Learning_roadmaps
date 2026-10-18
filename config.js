// Dual Track settings. Edit this file on GitHub, then commit.
window.DUAL_TRACK_CONFIG = {

  // 1) Accounts: your Supabase (PostgreSQL) project.
  //    Supabase dashboard > Project Settings > API: the Project URL and the "anon public" key.
  //    The anon key is meant to be public. The rules in supabase/setup.sql protect the data.
  //    Set this back to null to run without accounts (progress saved only in each browser).
  supabase: {
    url: "https://asbejkuqsbhohkcjczvb.supabase.co",
    anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzYmVqa3Vxc2Job2hrY2pjenZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIzMTYwNzYsImV4cCI6MjEwNzg5MjA3Nn0.k9y1Eu-RDoxwPW9yoTZciOHNqA1X5LPaa6mHVptv5h0"
  },

  // 2) Admins are set in the database: the ADMIN EMAIL line in supabase/setup.sql.

  // 3) Optional. Video links if you are NOT using accounts (with accounts, add them on the Admin page).
  //    Example: { 1: "https://youtu.be/xxxxxxxxxxx", 2: "https://youtu.be/yyyyyyyyyyy" }
  videoLinks: {}
};
