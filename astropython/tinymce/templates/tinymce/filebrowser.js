function djangoFileBrowser(field_name, url, type, win) {
    var filter_type = "";

    switch(type) {
        case 'image': filter_type = "Image"; break;
        case 'media': filter_type = "Video"; break;
    }
    
    var url = "{{ fb_url }}?popup=1&pop=2&type=" + type;

    var nw = tinyMCE.activeEditor.windowManager.open(
        {
            'file': url,
            'width': 820,
            'height': 500,
            'resizable': "yes",
            'movable': "yes",
            'scrollbars': "yes",
            'inline': "yes",
            'close_previous': "no"
        },
        {
            'window': win,
            'input': field_name,
            'editor_id': tinyMCE.activeEditor.id
        }
    );

    return false;
}
