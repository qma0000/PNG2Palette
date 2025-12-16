# PNG2Palette
Converts 64x64 png file into [send/receive by Snowfro](https://www.artblocks.io/marketplace/collections/sendreceive-by-snowfro)'s hex string for import/export image.

Known issue: 
1.colors with less saturation tends to mapped with grayscale color. 
2.the resulting pixel will be transparent only if the pixel in the input png has alpha value of 0.

Therefore, further inspection and remapping grayscale color might be needed for the better description. 

## Required Library
[NumPy](https://numpy.org/)  
[PIL](https://pypi.org/project/pillow/)  

## Usage
```bash
usage: python png_to_palette [input_png] [hex string text file (default:hex.txt)]
       make sure the input is 64x64 png file.
       copy hex string into send/receive's hex string import form.
```


