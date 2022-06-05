from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

url = "https://r3---sn-npoeen7k.c.drive.google.com/videoplayback?expire=1587033354&ei=yvyXXr2PM-WBmvUPt_uPyA8&ip=27.34.91.142&cp=QVNNWUFfUlNTRVhOOk1WTlFTTjJPRXE1Uk40eGZabWZQVUFHWEdjOFNmbmVNVmg3cmh3czZXVDU&id=5f6b79c175b0f93a&itag=22&source=webdrive&requiressl=yes&sc=yes&ttl=transient&susc=dr&driveid=1zSwTzZS0vqGSVyElbQFnKCxtgv30K3D7&app=texmex&mime=video/mp4&dur=1434.319&lmt=1586517615999309&sparams=expire,ei,ip,cp,id,itag,source,requiressl,ttl,susc,driveid,app,mime,dur,lmt&sig=AJpPlLswRQIhAPXADiKs37yf_sCCgmuR9OBI9XDSeC2FrPck7Q-FjpUoAiB9HkXs9HtrkJb2RlxpSEb1IVN5kzNKFCw0Lfl7nlHA5Q==&cpn=vivLW6pXjX2lb7_9&c=WEB_EMBEDDED_PLAYER&cver=20200415&redirect_counter=1&cm2rm=sn-cvhlr7s&req_id=a2964d64cd9136e2&cms_redirect=yes&mh=po&mm=34&mn=sn-npoeen7k&ms=ltu&mt=1587018485&mv=u&mvi=2&pl=21&lsparams=mh,mm,mn,ms,mv,mvi,pl,sc&lsig=ALrAebAwRAIgEGzUpt1uduI1lJoDQ2D4Bl8rj7UYb59pTj1m_qUMXFgCIBEoYpBH_-jVUG9yUXo0mlKe1mNT09GcL_H5oMZoPJF2"
hostName = "127.0.0.1"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.headers['range']):
            customheader = {'Cookie' : 'DRIVE_STREAM=muVKLvfIeDY; ANID=AHWqTUlucAkvZQgXzJf3qNbiac5hIDSrT3lDQoV3lDdJuuHVoZYBpo7leQnWiIuy; NID=202=VOnZuZywRcJGbLAgtGythcKBZQ1_lD8OhntFubu-Iz_u-Qo-ej9PbGfDOOnAi-0qNvAZ2M2dZUJeZbe8ihCkmk4j8yOu_bfrK_b6xTCDvHCy-ifY1qDi_vbCCxkQqvDNhSjXEYBfi7G7n23ixM5qYZiLZYzRmXmSfZDy3KfIH1I; 1P_JAR=2020-4-16-6', 'Range' : self.headers['range']}
        else:
            customheader = {'Cookie' : 'DRIVE_STREAM=muVKLvfIeDY; ANID=AHWqTUlucAkvZQgXzJf3qNbiac5hIDSrT3lDQoV3lDdJuuHVoZYBpo7leQnWiIuy; NID=202=VOnZuZywRcJGbLAgtGythcKBZQ1_lD8OhntFubu-Iz_u-Qo-ej9PbGfDOOnAi-0qNvAZ2M2dZUJeZbe8ihCkmk4j8yOu_bfrK_b6xTCDvHCy-ifY1qDi_vbCCxkQqvDNhSjXEYBfi7G7n23ixM5qYZiLZYzRmXmSfZDy3KfIH1I; 1P_JAR=2020-4-16-6'}
        video = requests.get(url, stream=True, headers=customheader)
        print("total time", video.elapsed.total_seconds())
        self.send_response(video.status_code)
        for i in video.headers:
            self.send_header(i,video.headers[i])
        self.end_headers()
        for line in video.iter_content(chunk_size=100000):
            if line:
                self.wfile.write(line)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")