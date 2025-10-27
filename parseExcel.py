import pandas as pd
import re
import sys

def search_excel(file_path, character_name, question):
    """
    Searches an Excel file for a given character and question.
    If any password (comma-separated) for the character is found in the question, returns the secret.
    Otherwise, returns the generic information.
    Also returns the description ('desc') the first time a character is encountered.
    If character_name is empty or not found, returns a list of all available characters.
    If character_name is provided but question is empty, returns the generic info for the character.

    Args:
        file_path (str): Path to the Excel file.
        character_name (str): Name of the character to filter rows.
        question (str): The question to check for passwords.

    Returns:
        str: Description, and either secret or generic info for the character,
             or a list of available characters if character_name is empty or not found.
    """
    df = pd.read_excel(file_path)

    required_columns = [
        "character", "desc", "reserved", "password", "generic", "secrets"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' does not exist in the Excel file.")

    # Convert all relevant columns and inputs to lowercase for better matching
    df["character"] = df["character"].astype(str).str.lower()
    df["desc"] = df["desc"].astype(str).str.lower()
    df["password"] = df["password"].astype(str).str.lower()
    df["generic"] = df["generic"].astype(str).str.lower()
    df["secrets"] = df["secrets"].astype(str).str.lower()
    character_name = character_name.lower()
    question = question.lower()

    # If character_name is empty or not found, return all available characters
    if not character_name or df[df["character"] == character_name].empty:
        characters = sorted(df["character"].dropna().unique())
        return "Available characters:\n" + "\n".join(characters)

    # Filter rows by character name
    character_rows = df[df["character"] == character_name]
    desc = character_rows.iloc[0]["desc"]

    # If question is empty, return generic info
    if not question:
        generic = character_rows.iloc[0]["generic"]
        return f"Character: {character_name}\nDescription: {desc}\nGeneric: {generic}"

    # Check for any password in the question (case-insensitive)
    found_secret = None
    for _, row in character_rows.iterrows():
        passwords = str(row["password"]).split(",")
        for pw in passwords:
            pw = pw.strip()
            if pw and re.search(re.escape(pw), question):
                found_secret = row["secrets"]
                break
        if found_secret:
            break

    if found_secret:
        return f"Character: {character_name}\nDescription: {desc}\nSecret: {found_secret}"
    else:
        generic = character_rows.iloc[0]["generic"]
        return f"Character: {character_name}\nDescription: {desc}\nGeneric: {generic}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test.py <character_name> [question]")
        sys.exit(1)
    
    file_path = "D:\\ollama\\quest.xlsx"
    character_name = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else ""
    print(search_excel(file_path, character_name, question))