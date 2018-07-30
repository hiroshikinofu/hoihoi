class Anime:
	"""
	お気に入りのアニメを登録する
	"""

	def __init__(self):
		self.favorite_animes = []

	def favorite(self, anime):
		"""
		アニメをお気に入りに登録する。
		すでに登録済みのアニメだった場合は追加しない

		:param str anime: お気に入りに登録するアニメのタイトル
		"""

		if anime not in self.favorite_animes:
			self.favorite_animes.append(anime)		#1

		return self

		#1 変数animeが、リストself.favorite_animesの内容と一致しない場合、
		#1 リストself.favorite_animesの末尾に変数animeを追加しろ

	def least_favorite(self, anime):
		"""
		アニメをお気に入りから削除する。
		未登録のアニメだった場合は例外を送出して呼び出し元へ知らせる

		:param str anime: お気に入りから削除するアニメのタイトル
		"""

		if anime in self.favorite_animes:
			self.favorite_animes.remove(anime)
		else:
			raise Exception('指定したアニメはお気に入りリストに存在しません')

		return self
