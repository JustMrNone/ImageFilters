from PIL import Image, ImageFilter
import sys

def main():
    before = get_file_name()
    choice = get_filter_choice()
    output_file_name = get_output_file_name()
    apply_filter(before, choice, output_file_name)
    
def get_file_name():
    while True:
        try:
            if len(sys.argv) <= 1:
                filen = input("Enter File Name (Make sure it is in the root directory, default is Image.png which is a picture of a banana): ")
            else:
                filen = sys.argv[1]
                
            if not filen.strip():
                filen = "Image.png"
                 
            before = Image.open(filen)
            return before
        
        except FileNotFoundError:
            print("No such file or directory, Please input a valid file name")
        except Exception as e:
            print(f"Something went wrong: {e}")

def get_filter_choice():
    print("Filters:\n1.BLUR\n2.CONTOUR\n3.DETAIL\n4.EDGE_ENHANCE\n5.EDGE_ENHANCE_MORE\n6.EMBOSS\n7.FIND_EDGES\n8.SHARPEN\n9.SMOOTH\n10.SMOOTH_MORE")
    while True:
        try:
            if len(sys.argv) <= 2:
                inputnum = int(input("Which filter do you want to apply? "))
            else:
                inputnum = int(sys.argv[2])
            
            if inputnum not in range(1, 11):
                raise ValueError
            
            return inputnum
        
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 10.")

def get_output_file_name():
    
    if len(sys.argv) == 4:
        name = sys.argv[3]
        if not name.strip() and len(sys.argv) <=4:
            name = "Picture"
    else:
        name = input("Enter the name for your new file (default is Picture): ")
        if not name.strip():
            name = "Picture"
    return name

def apply_filter(before, choice, name):
    filters = {
        1: (ImageFilter.BLUR, f"{name}(BLUR).jpg"),
        2: (ImageFilter.CONTOUR, f"{name}(CONTOUR).jpg"),
        3: (ImageFilter.DETAIL, f"{name}(DETAIL).jpg"),
        4: (ImageFilter.EDGE_ENHANCE, f"{name}(EDGE_ENHANCE).jpg"),
        5: (ImageFilter.EDGE_ENHANCE_MORE, f"{name}(EDGE_ENHANCE_MORE).jpg"),
        6: (ImageFilter.EMBOSS, f"{name}(EMBOSS).jpg"),
        7: (ImageFilter.FIND_EDGES, f"{name}(FIND_EDGES).jpg"),
        8: (ImageFilter.SHARPEN, f"{name}(SHARPEN).jpg"),
        9: (ImageFilter.SMOOTH, f"{name}(SMOOTH).jpg"),
        10: (ImageFilter.SMOOTH_MORE, f"{name}(SMOOTH_MORE).jpg")
    }
    
    filter_to_apply, output_file = filters[choice]
    after = before.filter(filter_to_apply)
    after.save(output_file)
    print(f"Filter applied. Image saved as {output_file}")

if __name__ == "__main__":
    main()
