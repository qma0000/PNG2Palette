from PIL import Image
import numpy as np
import math
import sys

def get_palette(palette_png = 'palette/palette.png'): 
    result = {}
    palette_image = Image.open(palette_png)
    palette_np = np.array(palette_image,dtype = np.float64)
    for i in range(4): #max 4 rows
        for j in range(64): #max 64 columns
            val = palette_np[16*i][16*j] #64x64 image -> 1024 x 1024 image
            if (64*i + j ) > 0: #first index: transparent, but shown as some gray color in palette.png
                result[64*i + j] = val
    return result
    
    
def get_image_as_palette(fpath = 'cirno_64x64.png'): #make sure that the input image is 64x64 image
    palette = []
    palette_array = [ [ -1 for i in range(64) ] for j in range(64)]
    image = Image.open(fpath)
    width, height = image.size
    if width != 64 or height != 64:
        print("Image is not 64 x 64. Current image size: %d X %d "%(width, height))
        raise ValueError
        
    image_np = np.array(image,dtype = np.float64)
    for i in range(64): 
        for j in range(64): 
            val = list(image_np[i][j])
            if val not in palette:
                palette.append(val)
            palette_idx = palette.index(val)
            palette_array[i][j] = palette_idx
    palette_np = [ np.array(p) for p in palette]        
    return palette_np, palette_array
    
def palette_match(palette_dict, palette_image): #for given palette_image, find the most similar color from palette_dict.  
    # key of palette_dict: 1 ~ 255
    p2p = [] #palette_image to palette_dict
    for p_im in palette_image:# np array of size: 4
        min_idx = 0
        min_diff = 999999999 
        if p_im[3] == 0: #transparent
           pass
        else:
            for i in range(1,256): #palette_dict key
                p_di = palette_dict[i]
                #calc_redmean
                r_mean = 0.5*(p_di[0]+p_im[0])
                diff = math.sqrt( (2+r_mean/256.0)*(p_im[0] - p_di[0])**2 + 4.0*(p_im[1] - p_di[1])**2 + (2+(255.0-r_mean)/256.0)*(p_im[2] - p_di[2])**2) 
                if diff < min_diff:
                    min_idx = i
                    min_diff = diff
        p2p.append(min_idx)
    return p2p    

def main():    
    if len(sys.argv) == 1:
        print("usage: python png_to_palette [input_png] [hex string text file (default:hex.txt)]")
        print("       make sure the input is 64x64 png file.")
        print("       copy hex string into send/receive's hex string import form")
        return
    elif len(sys.argv) == 2:
        palette_png = sys.argv[1]
        string_fpath = 'hex.txt'
    elif len(sys.argv) == 3:
        palette_png = sys.argv[1]
        string_fpath = sys.argv[2]
    
    palette_dict = get_palette(palette_png = 'palette/palette.png')
    palette_image, palette_array = get_image_as_palette(fpath = palette_png)
    p2p = palette_match(palette_dict, palette_image)
    result =[]
    for i in range(64): 
        for j in range(64):
            result.append('{:02X}'.format(p2p[palette_array[i][j]]))
    result_str = "".join(result)

    with open(string_fpath,'w') as file:
        file.write(result_str)
    return
main()


