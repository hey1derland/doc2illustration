from diffusers import StableDiffusionPipeline, DiffusionPipeline
import torch
import sys
import argparse
import re, os
from bart_summary import summary_api, do_summary_and_save_results


def main(args):
    model = args.model
    character_list = args.character
    text_path = args.summary
    pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float32).to("cuda")
    bart_model = "facebook/bart-large-xsum"
    
    api = summary_api(bart_model)
    summary = do_summary_and_save_results(api=api, text_path=text_path)

    for i, line in enumerate(summary):
        # text preprocessing
        print(line)
        prompt = re.sub(r'[^\w\s]', '', line).strip()
        prompt = re.sub('[.]', ',', prompt).strip()
        print(line)
        # replace a character name to token
        for character in character_list:
            prompt = prompt.replace(character, 'a photo of xzzxy person')
        
        # add tags
        tags = "very cute illustration for a children's book, digital art, highly detailed, rim light, exquisite lighting, clear focus, very coherent, details visible, soft lighting, character design, concept, atmospheric, fluffy, vibrant colors, trending on artstation, foggy, sun flare"
        final_prompt = f'{prompt}, {tags}'
)
        # generate images
        negative_prompts = 'text, watermark, duplicate, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, blurred, grainy'
        num_images_per_prompt = 4
        image_l = pipe(final_prompt, num_inference_steps=120, guidance_scale=7.5, negative_prompt = negative_prompts,
                    num_images_per_prompt=num_images_per_prompt).images
        
        # save images
        save_folder_name = args.summary.split('/')[-1].split('.txt')[0]
        save_folder_path = f'/data4/heywon/webtoon/diffusers/examples/dreambooth/t2i_results2/{save_folder_name}'
        model_name = model.split('/')[-1]
        if not os.path.isdir(f'{save_folder_path}/{model_name}/line{i}'):
            os.makedirs(f'{save_folder_path}/{model_name}/line{i}')
            
        for j, image in enumerate(image_l):
            image.save(f'{save_folder_path}/{model_name}/line{i}/{j}.png')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m')
    parser.add_argument('--summary', '-s')
    parser.add_argument('--character', '-c', nargs='+', default = ['Pinocchio'])
    args = parser.parse_args()
    main(args)
