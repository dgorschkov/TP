import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    response = vk.friends.get(fields="bdate, city")
    if response['items']:
        data = [(item['last_name'], item['first_name'], item.get('bdate', 'None')) for item in response['items']]
        for item in sorted(data):
            print(*item)


if __name__ == '__main__':
    main()
