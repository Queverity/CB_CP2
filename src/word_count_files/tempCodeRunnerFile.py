    document = parse_document(file_path)
                while True:
                    action = input("What would you like to do?\n1. Save Document\n2. View Document and Word Count\n3. Add content to document\n4. Exit\nEnter Number:\n")
                    match action:
                        case "1":
                            update_document(file_path,document)
                            continue
                        case "2":
                            display_text(document)
                            continue
                        case "3":
                            new_text = input_text(document)
                            for i in new_text:
                                document.append(i)
                            continue
                        case "4":
                            print("Are you sure you want to exit?")
                            keep_going = input("Y/N:\n").strip().capitalize()
                            if keep_going == "Y":
                                continue
                            else:
                                break
                        case _:
                            print("Please enter 1, 2, 3, or 4.")
                            continue
                break