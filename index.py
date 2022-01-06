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
	def get_css(self, css: str) -> str:
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
		else:
			#404 Error
	def get_body(self) -> str:
		return "<body>"+''.join(str(x) for x in self.body)+"</body>"
	def get_html(self) -> str:
		return "<html>"+self.get_head()+self.get_body()+"</html>"

"""class Template:
	def __init__(self, html: str, css: str):
		fhtml = open(html)
		self.html = fhtml.read()
		fhtml.close()
		fcss = open(css)
		self.css = fcss.read()
		fcss.close()
		self.md = ""
		self.mdexists = False
		self.class = ""
	def set_MD(path: str):
		if (os.path.exists(path)):
			fmd = open(path)
			self.md = fmd.read()
			fmd.close()
			print("reading MD at "+path)
			self.mdexists = True
		else:
			fmd = open("md/404.md")
			self.md = fmd.read()
			fmd.close()
			self.mdexists = True
	def set_class(class: str):
		self.class = class
	def get_page():
		if not this.mdxists:
			#404
		return self.html + "<style>" + self.css + "</style" + "<div class=\"" + self.class + "\">"#+md+"</div>"""

fhtml = open("html/tb.html")
fcss = open("css/style.css")
page = HTMLDoc(fhtml.read(), fcss.read())
fhtml.close()
fcss.close()

@app.route("/")
def hello():
	return html

if __name__ == "__main__":
	app.run()
