
examples=(
	'/data/sandor/images/monopointcloud/multiview/input/view_1'
    '/data/sandor/images/monopointcloud/multiview/input/view_2'
)

for i in "${examples[@]}"; do
	filename=$(basename "$i")
    echo "Processing $filename"
	bash scripts/textual_inversion/textual_inversion.sh 0 runwayml/stable-diffusion-v1-5 "$i"/rgba.png out/textual_inversion/${filename} _nerf_${filename}_ statue --max_train_steps 3000
done

# device=$1
# bash scripts/textual_inversion/textual_inversion.sh $device runwayml/stable-diffusion-v1-5 data/demo/blackpink-lisa/image.png out/textual_inversion/data/demo/blackpink-lisa _blackpink_lisa_ lisa --max_train_steps 3000

# bash scripts/textual_inversion/textual_inversion.sh $device runwayml/stable-diffusion-v1-5 data/demo/blackpink-lisa/image.png out/textual_inversion/data/demo/a-fullbody-ironman _ironman_ ironman --max_train_steps 3000

# bash scripts/textual_inversion/textual_inversion.sh $device runwayml/stable-diffusion-v1-5 data/demo/taylor-swift-sit-1989/image.png out/textual_inversion/data/demo/taylor-swift-sit _taylor_swift_sit_ taylor --max_train_steps 3000
# bash scripts/textual_inversion/textual_inversion.sh $device runwayml/stable-diffusion-v1-5 data/demo/taylor-swift-in-red-hat-blue-t-shift-light-green-skirt-long-black-sock-red-high-heel-shoe-with-a-blue-bag/image.png out/textual_inversion/data/demo/taylor-swift2 _taylor_swift_2_ taylor --max_train_steps 3000
# bash scripts/textual_inversion/textual_inversion.sh 0 runwayml/stable-diffusion-v1-5 /data/sandor/images/barbie/barbie.png /data/sandor/images/barbie/barbie_token _barbie_ barbie --max_train_steps 3000
# bash scripts/textual_inversion/textual_inversion.sh 0 runwayml/stable-diffusion-v1-5 /data/sandor/images/monopointcloud/statue_full/statue.png /data/sandor/images/monopointcloud/statue_full/statue_token _statue_ statue --max_train_steps 3000