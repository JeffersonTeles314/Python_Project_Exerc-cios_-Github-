uniform float iGlobalTime;

varying vec2 fragCoord;

float rand(vec3 n){
return fract(abs(sin(dot(n,vec3(4.3357,-5.8464,6.7645))*52.47))*256.75+0.325);
}

void main(void){
	vec3 p = vec3(fragCoord.xy+vec2(iGlobalTime)*64.0,0.0);
	float b = (rand(floor(p/64.0))*0.5+rand(floor(p/32.0))*0.3+rand(floor(p/16.0))*0.2);
	gl_FragColor = vec4(vec3(b*0.6),1.0);
	}

