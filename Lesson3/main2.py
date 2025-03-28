from oop import AnimeItem
import json, os

# Khởi tạo đối tượng
a1 = AnimeItem(1, 'One Piece', '01/01/2001')
a2 = AnimeItem(2, 'Naruto', '01/01/2002')

# Trả về thư mục hiện tại
print(os.getcwd())

# Viết đối tượng vào file
    # with open(): dùng để mở, tự động đóng sau khi thực hiện
    # 'w': ghi file, nếu file không có sẽ tạo file mới
    # 'anime.json': tên file, nếu chưa có sẽ tự động tạo
with open('anime.json', 'w') as file:
    # json.dump(): chuyển đối tượng thành chuỗi JSON
    json.dump(a1.__dict__, file)

# Đọc dữ liệu
with open('anime.json', 'r') as file:
    data = json.load(file)
    loaded_data = AnimeItem(data['id'], 
                            data['title'],
                            data['release_date'])
print(loaded_data.title)

# Đọc nhiều đối tượng từ file json
with open('anime2.json', 'r') as file:
    anime_data = json.load(file)

# Danh sách anime
anime_list = list()
for item in anime_data:
    anime = AnimeItem(  item['id'], 
                        item['title'],
                        item['release_date'] )
    anime_list.append(anime)

# Hiện data để kiểm tra
for item in anime_list:
    print(f'{item.title} - {item.release_date}')