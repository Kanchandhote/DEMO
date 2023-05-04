<script>
    $('.action_td').on('click', '.file_select_btn', function() {
        $(this).siblings('input[type="file"]').click(); 
    });

    $(document).on('change', '.excel_upload_input', function() {
        var file_input = $(this);

        var form_data = new FormData();
        form_data.append('report_id', $(this).data('bulk_id'));
        form_data.append('report_file', $(this).prop('files')[0]);
        
        
        $.ajax({
            url: '<?php echo base_url('reports/upload_corrected_report'); ?>',
            type: "POST",
            dataType: 'json',
            data: form_data,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            beforeSend: function(){
                $(file_input).attr('disabled', true);
                $(file_input).siblings('input[type="file"]').attr('disabled', true);
                $(file_input).html('<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span><span class="ml-25 align-middle">Loading...</span>');
            },
            complete: function(response){
                alert(response.responseJSON.msg);
                if(response.responseJSON.success){
                    location.reload();   
                }

                $(file_input).attr('disabled', false);
                $(file_input).siblings('input[type="file"]').attr('disabled', false);
                $(file_input).html('<i data-feather="file"></i>Upload Corrected Excel');
                $(file_input).val('');
            }
        });
    });

    $(document).on('click', '.publish_report_btn', function() {
        var this_btn = $(this);
        var form_data = new FormData();
        form_data.append('report_id', $(this).data('bulk_id'));
        
        
        $.ajax({
            url: '<?php echo base_url('reports/publish_report'); ?>',
            type: "POST",
            dataType: 'json',
            data: form_data,
            processData: false,
            contentType: false,
            beforeSend: function(){
                $(this_btn).attr('disabled', true);
                $(this_btn).html('<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span><span class="ml-25 align-middle">Loading...</span>');
            },
            complete: function(response){
                alert(response.responseJSON.msg);
                if(response.responseJSON.success){
                    location.reload();   
                }

                $(this_btn).attr('disabled', false);
                $(this_btn).html('Publish');
            }
        });
    });

    $('.admin_report_table').DataTable({
        "searching": true,
        "info": true,
        "ordering": false,
        "lengthChange": false,
        "pageLength": 20,
    });



</script>