#!/bin/python
""" Webilangue-Py - Gabriel Bauer (@ToCodeABluejay)
 
  Copyright (c) 2021 Gabriel Bauer (@ToCodeABluejay)
 
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
 
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
 
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
 """
from flask import Flask
import os
import copy

supported_languages = ["en", "fr"]

app = Flask(__name__)

class HTMLDoc:
	def __init__(self, head: list or str, body: list or str):
		if isinstance(head, str):
			self.head = [head]
		else:
			self.head = head
		if isinstance(body, str):
			self.body = [body]
		else:
			self.body = body
	def get_css(css: str) -> str:
		return "<style>"+css+"</style>"
	def set_head(self, head: list or str) -> None:
		if isinstance(head, str):
			self.head = [head]
		else:
			self.head = head
	def add_head(self, head: list or str) -> None:
		if isinstance(head, str):
			self.head.append(head)
		else:
			self.head += head
	def get_head(self) -> str:
		return "<head>"+''.join(str(x) for x in self.head)+"</head>"
	def set_body(self, body: list or str) -> None:
		if isinstance(body, str):
			self.body = [body]
		else:
			self.body = body
	def add_body(self, body: list or str) -> None:
		if isinstance(body, str):
			self.body.append(body)
		else:
			self.body += body
	def add_MD(self, md: str) -> None:
		if (os.path.exists(md)):
			fmd = open(md)
			self.add_body(fmd.read())
			fmd.close()
		#else:
			#404 Error
	def get_body(self) -> str:
		return "<body>"+''.join(str(x) for x in self.body)+"</body>"
	def get_html(self) -> str:
		return "<html>"+self.get_head()+self.get_body()+"</html>"

fhtml = open("html/tb.html")
fcss = open("css/style.css")
page = HTMLDoc(fhtml.read(), HTMLDoc.get_css(fcss.read()))
fhtml.close()
fcss.close()

@app.route("/", methods = ['POST', 'GET'])
def hello():
	return page.get_html()

@app.route("/<string:path>/", methods = ['POST', 'GET'])
def path(path):
	lang = request.accept_languages.best_match(supported_languages)
	ret = copy.deepcopy(page)
	ret.add_MD("md/"+path+"."+lang+".md")
	return ret.get_html()

if __name__ == "__main__":
	app.run()
