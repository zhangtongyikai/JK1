/*drop table IF EXISTS array_cn;
CREATE TABLE array_cn (
	samp_id varchar(63) NOT NULL,
	gene_sym varchar(31) NOT NULL,
	value_log2 double NOT NULL,
	primary key (samp_id,gene_sym),
	index (gene_sym)
);*/

/*LOAD DATA LOCAL INFILE "/EQL1/TCGA/GBM/array_cn/TCGA_GBM_CNA_SNP6_tumorOnly.dat" INTO TABLE array_cn;*/
/*LOAD DATA LOCAL INFILE "/EQL1/NSL/CGH/array_cn_NSL_GBM_109.dat" INTO TABLE array_cn;*/
/*LOAD DATA LOCAL INFILE "/EQL1/NSL/CGH/CGH_352_363.dat" INTO TABLE array_cn;*/
LOAD DATA LOCAL INFILE "/EQL1/NSL/CGH/IRCR_GBM14_591.dat" INTO TABLE array_cn;
