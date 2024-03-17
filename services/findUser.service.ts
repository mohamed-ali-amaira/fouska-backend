import { SupabaseClient } from "@supabase/supabase-js";

const findUser = async (client: SupabaseClient, phone: string) => {
  try {
    const { data: users, error } = await client
      .from("users")
      .select("*")
      .eq("phone", phone);

    // if error, throw error returning null & disabeling authentication for the users
    if (error) throw error;
    // if a number of users with the same phone exists return the same
    if (users && users.length > 0) {
      return users[0];
    }
    return null;
  } catch (error) {
    return null;
  }
};
