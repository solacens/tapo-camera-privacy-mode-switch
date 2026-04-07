import datetime
import http.server
import socketserver

import camera

PORT = 8080

if __name__ == "__main__":
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_message = b"{\"status\": \"ok\"}"
            self.wfile.write(response_message)

        def do_POST(self):
            now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                post_data = post_data.decode('utf-8')

                if post_data.lower() in ['true', 'y', 'yes', 'on']:
                    target_privacy_mode = True
                elif post_data.lower() in ['false', 'n', 'no', 'off']:
                    target_privacy_mode = False
                else:
                    raise Exception(f"invalid data [{post_data}]")

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                response_message = ("{\"status\": \"ok\", \"current_privacy_mode_state\": " + str(target_privacy_mode).lower() + "}").encode()
                self.wfile.write(response_message)

                camera.set_privacy_mode(target_privacy_mode)
                print(f"[{now}] Turning {"on" if target_privacy_mode else "off"} privacy mode.")

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                response_message = ("{\"status\": \"internal server error\", \"reason\": \"" + str(e) + "\"}").encode()
                self.wfile.write(response_message)
                print(f"[{now}]", e)


    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Started server at port {PORT}.")
        httpd.serve_forever()
