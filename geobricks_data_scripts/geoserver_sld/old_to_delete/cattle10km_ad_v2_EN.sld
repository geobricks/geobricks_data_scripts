<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>20120812</sld:Name>
            <sld:Title/>
                <FeatureTypeStyle>
                   <Rule>
                     <RasterSymbolizer>
                       <ColorMap type="intervals">
                         <ColorMapEntry color="#38A800" quantity="0.0000000000001" opacity="0.00000000000001" label="Heads"/>
                         <ColorMapEntry color="#8BD100" quantity="42.67" label="&gt;0 - 42.67" />
                         <ColorMapEntry color="#FFFF00" quantity="85.35" label="42.67 - 85.35"/>
                         <ColorMapEntry color="#FF7F00" quantity="128.036" label="85.35 - 128.03"/>
                         <ColorMapEntry color="#FF0000" quantity="10883.08" label="128.03 – 10,883.08"/>
                       </ColorMap>
                     </RasterSymbolizer>
                   </Rule>
               </FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>