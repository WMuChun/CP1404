import wikipedia

def main():
    search_term = input("Enter a page title or search phrase: ")
    while search_term != "":
        try:
            page = wikipedia.page(search_term, autosuggest=False)
            print("Page Title: ", page.title)
            print("Page Summary: ", wikipedia.summary(search_term))
            print("Page URL: ", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Your search term '{search_term}' resulted in multiple possibilities. Here are some suggestions: ")
            for option in e.options[:5]:
                print(option)
        except Exception as e:
            print(str(e))
        search_term = input("\nEnter a page title or search phrase: ")

if __name__ == "__main__":
    main()
