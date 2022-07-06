import requests

# Задание 1
class SuperHero:

    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.stats = {}

    def get_link_all(self):

        return 'https://akabab.github.io/superhero-api/api/'

    def get_id(self):
        response = requests.get(self.get_link_all() + 'all.json')
        all_superheros = response.json()
        for superhero in all_superheros:
            if self.name == superhero['name']:
                self.id = str(superhero['id'])
        print(f'ID супергероя: {self.id}')

    def get_stats(self):
        response = requests.get(self.get_link_all() + 'powerstats/' + self.id + '.json')
        self.stats = response.json()


def smartest_sup(*superheros):
    id = {}
    intelligence_sup = {}
    for superhero in superheros:
        intelligence = superhero.stats['intelligence']
        intelligence_sup.setdefault(superhero.name, intelligence)
        id.setdefault(superhero.name, superhero.id)
    the_smartest = max(intelligence_sup, key=intelligence_sup.get)

    return f'Самый умный супергерой - {id[the_smartest]}: {the_smartest}\n'

hulk = SuperHero('Hulk')
captain = SuperHero('Captain America')
thanos = SuperHero('Thanos')

hulk.get_id()
captain.get_id()
thanos.get_id()
hulk.get_stats()
captain.get_stats()
thanos.get_stats()
print(smartest_sup(hulk, captain, thanos))

# Задание 2
class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_link(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }
        params = {'path': '/test1', 'overwrite': 'true'}
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def upload_file(self, path):
        response_href = self.get_link()
        href = response_href.get('href', '')
        response = requests.put(href, data=open(path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен')

if __name__ == '__main__':
    path = '/Users/Olka1302/PycharmProjects/requests'
    TOKEN = ''
    yandex_disk = YaUploader(TOKEN)
    yandex_disk.upload_file(path)

