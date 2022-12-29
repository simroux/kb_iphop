/*
A KBase module: kb_iphop
This sample module contains one small method that filters contigs.
*/

module kb_iphop {

    /* Parameters for the iPHoP predict (predict) run.
        Required:
        viral genomes: A reference to the input viral genomes to process
        workspace_id: The integer workspace ID where the results will be saved.
    */
    typedef structure {
        int workspace_id;
        string viral_genomes_ref;
        int min_score;
        int no_qc;
    } iPHoP_Params;

    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kb_iphop(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
