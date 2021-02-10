# Bash
- [Pipes and Redirection](#pipes-and-redirection)

## Pipes and Redirection
|Symbol|Function|
|------|------|
||     |Pipe                             |
|>     |Output redirection (truncate)    |
|>>    |Output redirection (append)      |
|<     |Input redirection                |
|<<    |Here document                    |

- Pipes: send the output of the one process to another
  - break output into pages
  ```bash
  | less
  ```
  - count number of lines in the file,  `wc` returns number of lines, word count, byte and characters count
  ```
  cat file.csv | wc
  ```

- Redirections: send streams to/from files
  ```bash
  ls > list.txt
  ```
  - add information to the end of existing file
  ```bash
  ls >> list.txt
  ```
  - redirect errors output: `2>`, standard output: `1>`
  ```bash
  ls /notreal 1>output.txt 2>error.txt
  ```
  - send input
  ```bash
  cat < list.txt
  ```
  - hear document: take all till see the limit string, for cases where 
  ```bash
  cat << EndOfText
  heredoc> This is a
  heredoc> multiline
  heredoc> text string
  heredoc> EndOfText
  This is a
  multiline
  text string
  ```
  
  
