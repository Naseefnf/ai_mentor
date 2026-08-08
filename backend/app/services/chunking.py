def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    step = chunk_size-overlap
    
    for i in range(0,len(words), step):
        chunk_words = words[i: i+ chunk_size]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        
    return chunks