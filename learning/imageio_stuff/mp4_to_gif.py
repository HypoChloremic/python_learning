import imageio
import os, sys

# class TargetFormat(object):
#     GIF = ".gif"
#     MP4 = ".mp4"
#     AVI = ".avi"

def convertFile(inputpath, outputpath):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputpath, fps=fps)
    for i,im in enumerate(reader):
        sys.stdout.write("\rframe {0}".format(i))
        sys.stdout.flush()
        writer.append_data(im)
    print("\r\nFinalizing...")
    writer.close()
    print("Done.")

if '__main__' == __name__:
    convertFile("C:\\Users\\Admin\\Documents\\prwork\\projects\\snipping-tool\\doc\\main.mp4", 
                "C:\\Users\\Admin\\Documents\\prwork\\projects\\snipping-tool\\doc\\main.gif")