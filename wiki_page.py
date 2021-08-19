# from mediawiki import MediaWiki
import wikipedia

wikipedia.set_lang('pt')
# mediaWiki = MediaWiki(lang='pt')

page = wikipedia.page(wikipedia.random(1))
random_wikipedia_page = page.url