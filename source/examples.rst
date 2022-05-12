********
Examples
********

Example. Build bag with dbGap info
##################################

.. code-block:: python
    import hubmapbags
    from datetime import datetime
    from pathlib import Path

    output_directory = 'cfdebdbags-' + datetime.today().strftime('%Y%m%d')
    if not Path(output_directory).exists():
        Path(output_directory).mkdir(parents=True, exist_ok=True)

    id = 'HBM666.FFFW.363'
    dbgap_study_id = 'phs002267'

    hubmapbags.magic.do_it( id, \
        overwrite=False, \ #
        dbgap_study_id=dbgap_study_id, \
        compute_uuids=False, \
        copy_output_to = output_directory, \
        instance='prod', \
        debug=True )