import imageio
import os, sys

def convertFile(inputpath, outputpath):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputpath, fps=fps)
    for i,im in enumerate(reader):
        if i%10 == 0: # will save every tenth frame
            print(f'Saving frame: {i}')
            writer.append_data(im)
    print("Finalizing...")
    writer.close()
    print("Done.")

if '__main__' == __name__:
    convertFile("\\projects\\snipping-tool\\doc\\main.mp4", 
                "\\projects\\snipping-tool\\doc\\main.gif")