require("dotenv").config();

import { createClient } from "@supabase/supabase-js";

// Initialize Supabase client
const supabaseUrl = process.env.SUPABASE_URL + "";
const supabaseKey = process.env.SUPABASE_ANON_KEY + "";
const supabase = createClient(supabaseUrl, supabaseKey);

// (async () => {
//   const user = await findUser(supabase, "1234345");

//   console.log(user);
// })();
