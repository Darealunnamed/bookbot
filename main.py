def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  char_count = get_num_characters(text)
  empty_list = []


  for key, value in char_count.items():
    new_dict = {"char": key, "num": value}
    empty_list.append(new_dict)
  
  empty_list.sort(reverse=True, key=sort_on)


  print("--- Begin report of books/frankenstein.txt ---\n")
  print(f"{num_words} words were found in the document\n")

  for item in empty_list:
    if item["char"].isalpha():
      print(f"The '{item["char"]}' character was found {item["num"]} times")
  print("\n--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_characters(string):
  lowered_string = string.lower()
  my_dict = {}
  for char in lowered_string:
    if char not in my_dict:
      my_dict[char] = 1
    else:
      my_dict[char] += 1
  return my_dict

def sort_on(dict):
  return dict["num"]


main()
