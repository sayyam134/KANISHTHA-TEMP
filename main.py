from audiocraft.models import MusicGen
import torch

# Load MusicGen model (on CUDA if available)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = MusicGen.get_pretrained('medium', device=device)

def generate_music(prompts):
    """
    Generate music from the list of text prompts.
    
    :param prompts: A list of text prompts (strings).
    :return: Generated music tensor.
    """
    res = model.generate(prompts, progress=False)
    return res

def save_music(output_path, generated_audio):
    """
    Save generated audio to a file.
    
    :param output_path: Path where the generated audio will be saved.
    :param generated_audio: Tensor output of generated audio.
    """
    model.save_wav(output_path, generated_audio)
