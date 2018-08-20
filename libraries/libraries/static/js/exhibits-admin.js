$(function(){
    // hide media & embed selectors originally, only show if they're selected
    let css = `<style>.js-media, .js-embed_code { display: none; }</style>`
    $('body').append(css)

    $('#id_exhibit_artwork-FORMS').change('.js-type', ev => {
        let select = $(ev.target)
        let type = select.val()
        let form = select.parents('ul.fields')

        if (type === 'audio') {
            form.find('.js-embed_code').hide()
            // form.find('.js-media').show()
        } else if (type === 'html') {
            form.find('.js-embed_code').show()
            // form.find('.js-media').hide()
        } else if (type === 'image') {
            form.find('.js-embed_code').hide()
            // form.find('.js-media').hide()
        } else if (type === 'video') {
            form.find('.js-embed_code').hide()
            // form.find('.js-media').show()
        }
    })
})
