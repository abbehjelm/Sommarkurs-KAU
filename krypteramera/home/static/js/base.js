$(document).ready(function () {




    $('body').on('click', '#togglePassword', function () {
        console.log('clicked')
        const password = document.querySelector('#encryptionkey');
        const type = password
            .getAttribute('type') === 'password' ?
            'text' : 'password';
        password.setAttribute('type', type);
        // Toggle the eye and bi-eye icon
        this.classList.toggle('bi-eye');
    });




    $('body').on('click', '.cryptationModeToggle', function (e) {
        $('.cryptationModeToggle').each(function () {
            $(this).prop('checked', false)
            $(this).removeClass('btn-orange')
            $(this).addClass('btn-outline-orange')
        })
        $(this).prop('checked', true)
        $(this).removeClass('btn-outline-orange')
        $(this).addClass('btn-orange')
        $(this).blur()

        var modeIndex = parseInt($(this).attr('arg')) 
        if (modeIndex == 0) {
            $('#encryptionForm').removeClass('d-none')
            $('#dencryptionForm').addClass('d-none')
        }
        else {
            $('#dencryptionForm').removeClass('d-none')
            $('#encryptionForm').addClass('d-none')        
        }
    })

    $('body').on('click', '.dummyLink', function (e) {
        e.preventDefault()
    })

    $('body').on('click','#chooseKeyModalLink',function (e) {
        e.preventDefault()
        $('#chooseKeyModal').modal('show')
    })

    $('body').on('click','#initVectorInfoModalLink',function (e) {
        e.preventDefault()
        $('#initVectorInfoModal').modal('show')
    })
    
})