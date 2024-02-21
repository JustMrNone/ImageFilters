from PIL import Image, ImageFilter
#getting file name as input
while True:
    try:
        filen = str(input("Enter File Name (Make sure it is in the root directory default is Image.png which is a picture of a banana): "))
        
        if filen == "":
            filen = "Image.png"    
        before = Image.open(filen)
        break
    
    except FileNotFoundError:
        print("No such file or directory, Please input a valid file name")
    except Exception as e:
        print("something went wrong")
        
#showing options
print("Filters:\n1.BLUR\n2.CONTOUR\n3.DETAIL\n4.EDGE_ENHANCE\n5.EDGE_ENHANCE_MORE\n6.EMBOSS\n7.FIND_EDGES\n8.SHARPEN\n9.SMOOTH\n10.SMOOTH_MORE")
#getting users choice
try: 
    inputnum = int(input("Which filter do you want to apply? "))
#fliters using PIL library
    if inputnum == 1:
        after = before.filter(ImageFilter.BLUR)
        after.save("BLUR.jpg")
    elif inputnum == 2:
        after = before.filter(ImageFilter.CONTOUR)
        after.save("CONTOUR.jpg")
    elif inputnum == 3:    
        after = before.filter(ImageFilter.DETAIL)
        after.save("DETAIL.jpg")
    elif inputnum == 4:
        after = before.filter(ImageFilter.EDGE_ENHANCE)
        after.save("EDGE_ENHANCE.jpg")
    elif inputnum == 5:
        after = before.filter(ImageFilter.EDGE_ENHANCE_MORE)
        after.save("EDGE_ENHANCE_MORE.jpg")
    elif inputnum == 6:
        after = before.filter(ImageFilter.EMBOSS)
        after.save("EMBOSS.jpg")
    elif inputnum == 7:
        after = before.filter(ImageFilter.FIND_EDGES)
        after.save("FIND_EDGES.jpg")
    elif inputnum == 8:
        after = before.filter(ImageFilter.SHARPEN)
        after.save("SHARPEN.jpg")
    elif inputnum == 9:
        after = before.filter(ImageFilter.SMOOTH)
        after.save("SMOOTH.jpg")
    elif inputnum == 10: 
        after = before.filter(ImageFilter.SMOOTH_MORE)
        after.save("SMOOTH_MORE.jpg")
    
    else:
        print(inputnum," is not a valid Input")
except ValueError: 
    print("Invalid input. Please enter a valid Integer.")
    
    
