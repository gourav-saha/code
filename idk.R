library("ggmsa")
protein_sequences <- system.file("extdata", "sample.fasta", package = "ggmsa")
ggmsa(protein_sequences, 300, 350, color = "Clustal", font = "DroidSansMono", char_width = 0.5, seq_name = TRUE )

ggmsa("~/Desktop/projects/Mitacs/Sequences/ERV1/ERV1.fasta",1, 200, char_width = 0.5, seq_name = T) + geom_seqlogo(color="Chemistry_AA") + geom_msaBar()

filelist <- list.files("~/Desktop/projects/Mitacs/Sequences/ERV1/", full.names = T)
for (file in filelist){
  
  if (!exists("ERV1")){
    ERV1 <- read.table(file, header=TRUE, sep="\t")
  }
  
  # if the merged dataset does exist, append to it
  if (exists("ERV1")){
    temp_dataset <-read.table(file, header=TRUE, sep="\t")
    ERV1<-rbind(ERV1, temp_dataset)
    rm(temp_dataset)
  }
  
}

ggmsa("~/Desktop/projects/Mitacs/Sequences/HRR25/HRR25.fasta", char_width = 0.5, seq_name = T) + geom_seqlogo() + geom_msaBar()
