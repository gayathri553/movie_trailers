print("Content-type:text/html \n")
import os
import webbrowser

main_head = '''
<!DOCTYPE html>
<html>
<head>
    
<p>Movie Trailers</p>

    <style>
    .one,.two,.three,.four{
    width:500px;
    height:500px;
    float:left;
    margin-left:100px;
    margin-top:20px;
    padding:20px;
  }
  p{
    color:darkmagenta;
    background-color: greenyellow;
    text-align:center;
    font-size:30px;
  }
  img{ 
        width:100%;
        height:100%;
       /* overflow: hidden;*/
  }
  .one:hover,.two:hover,.three:hover,.four:hover{
    background-color:greenyellow;
    padding:40px;
    cursor:pointer;
    border-radius: 20%;
  }
  .onit {
    position: relative; 
    bottom: 20px; 
 /* Black see-through */
    opacity:0;
    color:darkmagenta;
    font-size: 30px;
    padding: 20px;
    text-align:center;

  }
  .one:hover .onit ,.two:hover .onit,.three:hover .onit,.four:hover .onit{
    opacity: 1;
  }

  .modal-footer button:hover{
      background-color:red;
  }
  
    </style>
    <title>Movie Trailer</title>
    <script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous">
    </script>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    
</head>

'''


main_content = '''
<body>
    <script>
        $(document).ready(function () {
            $("#myModal").on("hidden.bs.modal", function () {
                $("#iframeYoutube").attr("src", "#");
            })
        })
        function change(video) {
            var iframe = document.getElementById("iframeYoutube");
            iframe.src = "https://www.youtube.com/embed/" + video;
            $("#myModal").modal("show");
        }
    
    </script>

    <div class="modal fade" id="myModal" tabindex="-1"   aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="modal-footer">
                        <button type="button" data-dismiss="modal">&times;</button>
                    </div>
                    <iframe id="iframeYoutube" width="555" height="350" src="" frameborder="1"></iframe>

                </div>
            
            </div>
        </div>
    </div>

</body>
</html>
'''


movie_title_content = '''
<div class="one" onclick=" change('{trailer_youtube_url}')">
        <img src="{poster_image_url}"/>
        <div class="onit">{title}</div>
    </div>
    
'''


def  create_movie(movies):
    content = ''
    for i in movies:
        content += movie_title_content.format(
            title = i.title,
            poster_image_url = i.poster_image_url,
            trailer_youtube_url= i.trailer_youtube_url
        )
    return content

def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html','w')
    rendered_content = create_movie(movies)
    output_file.write(main_head + rendered_content+main_content)
    output_file.close()

    url =os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

    
