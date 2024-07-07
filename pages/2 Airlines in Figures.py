import streamlit as st
import streamlit.components.v1 as components

# Title of the Streamlit app
st.title('Airlines in Figures')

def main():
    html_temp = '''
    <div class='tableauPlaceholder' id='viz1720256591130' style='position: relative'>
        <noscript>
            <a href='#'><img alt='Airlines in Figures' src='https://public.tableau.com/static/images/SB/SB4CNNBDF/1_rss.png' style='border: none' /></a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='path' value='shared/SB4CNNBDF' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/SB/SB4CNNBDF/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='es-ES' />
            <param name='filter' value='publish=yes' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1720256591130');
        var vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width='100%';
        vizElement.style.height=(window.innerHeight - 100)+'px';
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    '''
    components.html(html_temp, width=2000, height=1500)

if __name__ == '__main__':
    main()