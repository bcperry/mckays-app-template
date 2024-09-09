import { clerkClient } from "@clerk/nextjs";
import { User } from "@clerk/nextjs/server";

export const getUser = async (userId: string): Promise<User | null> => {
  try {
    const user = await clerkClient.users.getUser(userId);
    return user;
  } catch (error) {
    console.error("Error fetching user:", error);
    return null;
  }
};