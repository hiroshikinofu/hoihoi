import unittest
from anime import Anime

class AnimeTest(unittest.TestCase):

	" easy_to_use_anime_instanceで生成したときの初期お気に入りリストのデータ "
	easy_to_use_anime_titles = ['成恵の世界', 'ぱにぽにだっしゅ！', 'らき☆すた']

	def easy_to_use_anime_instance(self):
		"""
		テストで使いやすいように初期データを登録したAnimeインスタンスを返す
		:return Anime
		"""
		anime = Anime()
		for anime_title in self.easy_to_use_anime_titles:
			anime.favorite(anime_title)
		return anime

	def test_single_call_favorite(self):
		"""
		favoriteメソッドを1回だけコールして正常に登録できたかテストする
		"""
		anime_title = '日常'
		anime = Anime()
		anime.favorite(anime_title)

		self.assertEqual(anime_title, anime.favorite_animes[0])

	def test_multiple_call_favorite(self):
		"""
		favoriteメソッドを複数回コールして正常に登録できたかテストする
		複数回コールは easy_to_use_anime_instance メソッドで実施している
		"""
		anime = self.easy_to_use_anime_instance()
		self.assertEqual(self.easy_to_use_anime_titles, anime.favorite_animes)


	def test_favorite_send_duplication_anime(self):
		"""
		お気に入りアニメのタイトルを重複して登録されないかテストする
		"""
		anime_title = '日常'
		anime = Anime()
		anime.favorite(anime_title)
		anime.favorite(anime_title)

		self.assertEqual(len(anime.favorite_animes), 1)
		self.assertEqual(anime_title, anime.favorite_animes[0])


	def test_least_favorite(self):
		"""
		お気に入りアニメリストから指定のアニメが正常に消えるかテスト
		easy_to_use_anime_instance を使って初期データを用意している。
		"""
		anime = self.easy_to_use_anime_instance()
		anime.least_favorite('ぱにぽにだっしゅ！')

		self.assertEqual(len(anime.favorite_animes), 2)
		self.assertEqual(['成恵の世界', 'らき☆すた'], anime.favorite_animes)


	def test_least_favorite_with_nodata(self):
		"""
		お気に入りアニメリストに存在しないアニメを削除しようとしたときに
		例外が送出されるかテスト
		"""
		anime = Anime()
		with self.assertRaises(Exception) as e:
			anime.least_favorite('日常')

		self.assertEqual('指定したアニメはお気に入りリストに存在しません', e.exception.args[0])
