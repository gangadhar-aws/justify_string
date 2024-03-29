
def justify_paragraph(paragraph, page_width):


    words = paragraph.split()
    lines = []
    current_line = words[0]


    for word in words[1:]:
        if len(word) > page_width:
            raise ValueError("Word '{}' is longer than the specified page width.".format(word))

        if len(current_line) + len(word) + 1 <= page_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line) 
    justified_lines = []
    for line in lines:
        words_in_line = line.split()
        if len(words_in_line) > 1:
            num_spaces = page_width - sum(len(word) for word in words_in_line)
            spaces_between_words = num_spaces // (len(words_in_line) - 1)
            extra_spaces = num_spaces % (len(words_in_line) - 1)
            justified_line = ''
            for i in range(len(words_in_line) - 1):
                justified_line += words_in_line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
            justified_line += words_in_line[-1]
        else:
            justified_line = words_in_line[0].ljust(page_width)
        justified_lines.append(justified_line)

    return justified_lines


def main():


    while True:
        paragraph= input("Enter The Paragraph :")
        if paragraph:
            break
        else:
            print("Error: Please enter a non-empty paragraph.")
    while True:         
        try:
            page_width = int(input("Enter The Page Width: "))
            lines = justify_paragraph(paragraph=paragraph, page_width=page_width)

            for i in lines:
                print(i)
            break
        except ValueError:
            print("Error: Please Enter a valid Page width integer.")
        except Exception as e:
            print("An unexpected error occurred.",e)
     
        
if __name__ == "__main__":
    main()
    