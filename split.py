import os, sys
from PIL import Image, ImageDraw

pic_path = "social-icons.png"
pic_row, pic_col = 8, 10
left, top = 79, 79
width = height = 89
margin = 31

icon_names = (
    "facebook;twitter;google+;instagram;vk;ok;linkedin;aboutme;slideshare;ello;"
    "youtube;youtube-play;vimeo;coub;medium;wordpress;tumblr;livejournal;pocket;rss;"
    "skype;phone;mail;send;send-light;map;yelp;foursquare;swarm;tripadvisor;"
    "pinterest;pinterest-light;behance;dribble;etsy;etsy-short;flikr;500px;vscogrid;photobucket;"
    "quora;stackoverflow;github;codepen;jsfiddle;habrahabr;producthunt;kickstarter;reddit;reddit-light;"
    "stumbleupon;delicious;digg;devianart;buffer;slack;messenger;snapchat;line-icon;line;"
    "angellist;xing;viadeo;upwork;envato;periscope;bookmate;shopify;favorite;like;"
    "apple;android;googleplay;windows;amazon;dropbox;googledrive;evernote;sketch;web"
).split(';')
icon_index = {name: divmod(i, pic_col) for i, name in enumerate(icon_names)}

outdir = 'split'


def draw_girds(pic, left, top, width, height, margin):
    """
    (for test only) Draw grids on the image for splitting it into icons.
    """
    draw = ImageDraw.Draw(pic)
    pic_w, pic_h = pic.size

    while left + width < pic_w or top + height < pic_h:
        draw.line((left, 0, left, pic_h), fill='black')
        draw.line((left+width, 0, left+width, pic_h), fill='black')
        draw.line((0, top, pic_w, top), fill='black')
        draw.line((0, top+height, pic_w, top+height), fill='black')
        left += width + margin
        top += height + margin
    pic.show()


def save_icon(name):
    try:
        row, col = icon_index[name]
    except KeyError:
        print(f"{name} is not in the icon list. See a full list:",
            '; '.join(sorted(icon_names)), sep="\n\n")
        exit()
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    output = os.path.join(outdir, f'{name}.png')

    with Image.open(pic_path) as im:
        # draw_girds(im, left, top, width, height, margin)
        box_left = left + col * (width + margin)
        box_top = top + row * (height + margin)
        box = (box_left, box_top, box_left + width, box_top + height)
        im.crop(box).save(output, "png")


# # Main:
# # Using example, crop the icon of 'facebook':
# #    python split.py facebook
#
# name = sys.argv[1]
# save_icon(name)

# Or you can save all icons at once:
for name in icon_names:
    save_icon(name)
