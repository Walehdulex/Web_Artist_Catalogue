import requests
import os
from flask import Flask, render_template, request

app = Flask(__name__)


class ArtistCatalog:
    def __init__(self):
        self.catalog = {
            'Michael Jackson': {'genre': 'Pop', 'rating': 9.5,
                                'image_url': 'http://m.gettywallpapers.com/wp-content/uploads/2022/01/Michael-Jackson-Wallpaper-768x1365.jpg',
                                'albums': [
                                    {'title': 'Thriller',
                                     'youtube_id': 'zzfZjXc-S_8&list=PLtZC5Fw8dg72eynmTSukbabRuPrm4Ix3W&ab_channel=FullAlbumMusic'},
                                    {'title': 'Off the Wall',
                                     'youtube_id': 'n3qQtSRmHxo&list=PLenFXOCc29OtFCpem8O38dYM5pqsovOi3&ab_channel=MichaelJackson-Topic'},
                                    {'title': 'Dangerous',
                                     'youtube_id': 'UGT_9ah_YFo&list=PLmKxR1vlf4cxoXWq4sv2hQdFUKGLsBisv&ab_channel=MichaelJackson-Topic'}]},
            'The Beatles': {'genre': 'Rock', 'rating': 9.4,
                            'image_url': 'https://www.grammy.com/_next/image?url=https%3A%2F%2Fi8.amplience.net%2Fi%2Fnaras%2Fthe-beatles_MI0003995354-MN0000754032&w=1080&q=75',
                            'albums': [
                                {'title': 'Abbey Road',
                                 'youtube_id': 'oolpPmuK2I8&list=PLFAcddgaFN8yWW7akMNXmxt7xtRTpS8kA&ab_channel=TheBeatles-Topic'},
                                {'title': 'Revolver',
                                 'youtube_id': 'l0zaebtU-CA&list=PLL-NbN8uTOijcKsr8WjBqh0tp4HS-Spua&ab_channel=TheBeatles-Topic'}]},
            'Bob Marley': {'genre': 'Reggae', 'rating': 9.0,
                           'image_url': 'https://ichef.bbci.co.uk/news/976/cpsprodpb/1342E/production/_118449887_gettyimages-3259910.jpg.webp',
                           'albums': [
                               {'title': 'Kaya',
                                'youtube_id': 'wlqB13iJu2o&list=PLnvVNd96RFMSMY3bhnS7feAGTOqrbEa6R&ab_channel=BobMarleyVEVO'},
                               {'title': 'Natty dread',
                                'youtube_id': 'fi-1Wnp0S84&list=PLnvVNd96RFMTQDJiy7mYLLmHW4bGxKhEz&ab_channel=BobMarley'}]},
            'Madonna': {'genre': 'Pop', 'rating': 8.7, 'image_url': 'https://w.forfun.com/fetch/8b/8bd03ab5979c15e821d54bf78ddce290.jpeg?h=900&r=0.5', 'albums': [
                {'title': 'True Blue',
                 'youtube_id': 'G333Is7VPOg&list=PLvHf4SnA7f8uxGJJ3LFduZa6TfdWnS37A&ab_channel=Madonna'},
                {'title': 'like a virgin',
                 'youtube_id': '6p-lDYPR2P8&list=PLvHf4SnA7f8ujT44W1Q49LV9GaMGv6kTS&ab_channel=Madonna'}]},
            'wizkid': {'genre': 'AfroPop', 'rating': 8.7, 'image_url': 'https://media.vogue.co.uk/photos/6041f07c107e7ce55db43e7d/2:3/w_2560%2Cc_limit/wiz.jpg','songs': [{'title': 'Made in lagos',
                 'youtube_id': 'qEEsc8j-FVI&list=PLsAk6h4n-dS3wtQOP_huuCDiCj3dnKp4E&ab_channel=WizkidVEVO'},
                {'title': 'Ayo',
                 'youtube_id': 'eF_CWfI481A&list=PLhwKLmzT3R18dW6Xc2JEZg2mgCZaGXlkx&ab_channel=Wizkid-Topic'}],'albums': [
                {'title': 'Made in lagos',
                 'youtube_id': 'qEEsc8j-FVI&list=PLsAk6h4n-dS3wtQOP_huuCDiCj3dnKp4E&ab_channel=WizkidVEVO'},
                {'title': 'Ayo',
                 'youtube_id': 'eF_CWfI481A&list=PLhwKLmzT3R18dW6Xc2JEZg2mgCZaGXlkx&ab_channel=Wizkid-Topic'}]},
            'Fela Kuti': {'genre': 'Afrobeat', 'rating': 9.3, 'image_url': 'https://wallpapercave.com/dwp1x/wp8156280.jpg', 'songs': [
                {'title': 'Zombie', 'youtube_id': 'rCISUKgPKRU&ab_channel=n3ph3sh'},
                {'title': 'Water No Get Enemy', 'youtube_id': 'IQBC5URoF0s&ab_channel=ACghigo'},
                {'title': 'Gentleman', 'youtube_id': 'snIV_-IECsM&ab_channel=n3ph3sh'},
                {'title': 'Sorrow Tears & Blood', 'youtube_id': 'jS7wPqEpwUQ&ab_channel=n3ph3sh'},
                {'title': 'Confusion', 'youtube_id': 'v2u1lPLFe0k&ab_channel=n3ph3sh'}]},
            'Tiwa Savage': {'genre': 'Afropop', 'rating': 9.1, 'image_url': 'https://newvision-media.s3.amazonaws.com/cms/866905a0-54ce-4c39-857e-e1f12250b7e2.jpg', 'songs': [
                {'title': 'Eminado', 'youtube_id': 'HxPqkwahxe0&ab_channel=officialtiwasavage'},
                {'title': 'My Love 3x', 'youtube_id': '_oSY4CYfXV4&ab_channel=officialtiwasavage'},
                {'title': 'All over', 'youtube_id': 'dFBQzRNsMK0&ab_channel=TiwaSavage'},
                {'title': 'wanted', 'youtube_id': 'HYJFTodtu5k&ab_channel=TiwaSavageVEVO'}]},
            'Burna Boy': {'genre': 'Afrofusion', 'rating': 9.0, 'image_url': 'https://crackmag.wpenginepowered.com/wp-content/uploads/2020/02/Issue-109-Cover-RGB-Web-scaled.jpg', 'songs': [
                {'title': 'Ye', 'youtube_id': 'lPe09eE6Xio&ab_channel=BurnaBoy'},
                {'title': 'Gbona', 'youtube_id': 'h7WfPHHXCAY&ab_channel=BurnaBoy'},
                {'title': 'On the Low', 'youtube_id': 'Ecl8Aod0Tl0&ab_channel=BurnaBoy'}, ]},
            'Drake': {'genre': 'World Music', 'rating': 8.9, 'image_url': 'https://wallpapercave.com/dwp1x/wp2742307.jpg', 'songs': [
                {'title': 'Hotline Bling', 'youtube_id': 'uxpDa-c-4Mc&ab_channel=DrakeVEVO'},
                {'title': 'God\'s Plan', 'youtube_id': 'xpVfcZ0ZcFM&ab_channel=DrakeVEVO'},
                {'title': 'In My Feelings', 'youtube_id': 'DRS_PpOrUZ4&ab_channel=DrakeVEVO'},
                {'title': 'Started From the Bottom', 'youtube_id': 'RubBzkZzpUA&ab_channel=DrakeVEVO'},
                {'title': 'One Dance', 'youtube_id': 'iAbnEUA0wpY&ab_channel=DrakeVEVO'}]},
            'Cardi B': {'genre': 'World Music', 'rating': 8.8, 'image_url': 'https://wallpapercave.com/wp/wp12546097.jpg', 'songs': [
                {'title': 'Bodak Yellow', 'youtube_id': 'PEGccV-NOm8&ab_channel=CardiB'},
                {'title': 'I Like It', 'youtube_id': 'xTlNMmZKwpA&ab_channel=CardiB'},
                {'title': 'WAP', 'youtube_id': 'hsm4poTWjMs&ab_channel=CardiB'},
                {'title': 'Up', 'youtube_id': '15Hq79BP2WU&ab_channel=CardiB'},
                {'title': 'Money', 'youtube_id': 'Zj2cK8wymIA&ab_channel=CardiB'}]},
            'Rihanna': {'genre': 'Jazz', 'rating': 8.7, 'image_url': 'https://wallpapercave.com/dwp1x/wp11991853.jpg', 'songs': [
                {'title': 'Umbrella', 'youtube_id': 'CvBfHwUxHIk&ab_channel=RihannaVEVO'},
                {'title': 'Diamonds', 'youtube_id': 'lWA2pjMjpBs&ab_channel=RihannaVEVO'},
                {'title': 'Only Girl (In The World)', 'youtube_id': 'pa14VNsdSYM&ab_channel=RihannaVEVO'},
                {'title': 'Work', 'youtube_id': 'HL1UzIK-flA&ab_channel=RihannaVEVO'},
                {'title': 'We Found Love', 'youtube_id': 'tg00YEETFzg&ab_channel=RihannaVEVO'}]},
        }

    def search(self, keyword):
        keyword = keyword.lower()
        results = []

        for artist, details in self.catalog.items():
            if keyword in artist.lower() or keyword in details['genre'].lower():
                results.append({
                    'artist': artist,
                    'genre': details.get('genre', 'N/A'),
                    'rating': details.get('rating', 'N/A'),
                    'image_url': details.get('image_url', ''),  # Add this line
                    'songs': details.get('songs', []),
                    'albums': details.get('albums', [])
                })
            elif 'songs' in details and any(keyword in songs['title'].lower() for songs in details['songs']):
                # If keyword matches any song title
                results.append({
                    'artist': artist,
                    'genre': details.get('genre', 'N/A'),
                    'rating': details.get('rating', 'N/A'),
                    'songs': [song for song in details['songs'] if keyword in song['title'].lower()],
                    'albums': details.get('albums', [])
                })

            elif 'albums' in details and any(keyword in album['title'].lower() for album in details['albums']):
                # If keyword matches any album title
                results.append({
                    'artist': artist,
                    'genre': details.get('genre', 'N/A'),
                    'rating': details.get('rating', 'N/A'),
                    'songs': details.get('songs', []),
                    'albums': [album for album in details['albums'] if keyword in album['title'].lower()]
                })

        return results


artist_catalog = ArtistCatalog()
search_history = []


@app.route('/song/<string:song>', methods=['GET'])
def song(song):
    # For simplicity, let's just pass the song name to the template
    return render_template('song.html', song=song)


@app.route('/album/<string:album>', methods=['GET'])
def album(album):
    # For simplicity, let's just pass the song name to the template
    return render_template('album.html', album=album)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        search_results = artist_catalog.search(user_input)

        # Add the search query to the history if there are results
        if search_results:
            search_history.append(user_input)

        return render_template('index.html', user_input=user_input, search_results=search_results,
                               search_history=search_history)

    return render_template('index.html', search_history=search_history)


if __name__ == '__main__':
    app.run(debug=True)
