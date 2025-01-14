// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContainerUploadArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerUploadArgs Empty = new ContainerUploadArgs();

    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with `content_base64` &amp; `source`
     * 
     */
    @Import(name="content")
    private @Nullable Output<String> content;

    /**
     * @return Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with `content_base64` &amp; `source`
     * 
     */
    public Optional<Output<String>> content() {
        return Optional.ofNullable(this.content);
    }

    @Import(name="contentBase64")
    private @Nullable Output<String> contentBase64;

    public Optional<Output<String>> contentBase64() {
        return Optional.ofNullable(this.contentBase64);
    }

    /**
     * If `true`, the file will be uploaded with user executable permission. Defaults to `false`.
     * 
     */
    @Import(name="executable")
    private @Nullable Output<Boolean> executable;

    /**
     * @return If `true`, the file will be uploaded with user executable permission. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> executable() {
        return Optional.ofNullable(this.executable);
    }

    /**
     * Path to the file in the container where is upload goes to
     * 
     */
    @Import(name="file", required=true)
    private Output<String> file;

    /**
     * @return Path to the file in the container where is upload goes to
     * 
     */
    public Output<String> file() {
        return this.file;
    }

    /**
     * A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with `content` &amp; `content_base64`
     * 
     */
    @Import(name="source")
    private @Nullable Output<String> source;

    /**
     * @return A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with `content` &amp; `content_base64`
     * 
     */
    public Optional<Output<String>> source() {
        return Optional.ofNullable(this.source);
    }

    /**
     * If using `source`, this will force an update if the file content has updated but the filename has not.
     * 
     */
    @Import(name="sourceHash")
    private @Nullable Output<String> sourceHash;

    /**
     * @return If using `source`, this will force an update if the file content has updated but the filename has not.
     * 
     */
    public Optional<Output<String>> sourceHash() {
        return Optional.ofNullable(this.sourceHash);
    }

    private ContainerUploadArgs() {}

    private ContainerUploadArgs(ContainerUploadArgs $) {
        this.content = $.content;
        this.contentBase64 = $.contentBase64;
        this.executable = $.executable;
        this.file = $.file;
        this.source = $.source;
        this.sourceHash = $.sourceHash;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerUploadArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerUploadArgs $;

        public Builder() {
            $ = new ContainerUploadArgs();
        }

        public Builder(ContainerUploadArgs defaults) {
            $ = new ContainerUploadArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param content Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with `content_base64` &amp; `source`
         * 
         * @return builder
         * 
         */
        public Builder content(@Nullable Output<String> content) {
            $.content = content;
            return this;
        }

        /**
         * @param content Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with `content_base64` &amp; `source`
         * 
         * @return builder
         * 
         */
        public Builder content(String content) {
            return content(Output.of(content));
        }

        public Builder contentBase64(@Nullable Output<String> contentBase64) {
            $.contentBase64 = contentBase64;
            return this;
        }

        public Builder contentBase64(String contentBase64) {
            return contentBase64(Output.of(contentBase64));
        }

        /**
         * @param executable If `true`, the file will be uploaded with user executable permission. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder executable(@Nullable Output<Boolean> executable) {
            $.executable = executable;
            return this;
        }

        /**
         * @param executable If `true`, the file will be uploaded with user executable permission. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder executable(Boolean executable) {
            return executable(Output.of(executable));
        }

        /**
         * @param file Path to the file in the container where is upload goes to
         * 
         * @return builder
         * 
         */
        public Builder file(Output<String> file) {
            $.file = file;
            return this;
        }

        /**
         * @param file Path to the file in the container where is upload goes to
         * 
         * @return builder
         * 
         */
        public Builder file(String file) {
            return file(Output.of(file));
        }

        /**
         * @param source A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with `content` &amp; `content_base64`
         * 
         * @return builder
         * 
         */
        public Builder source(@Nullable Output<String> source) {
            $.source = source;
            return this;
        }

        /**
         * @param source A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with `content` &amp; `content_base64`
         * 
         * @return builder
         * 
         */
        public Builder source(String source) {
            return source(Output.of(source));
        }

        /**
         * @param sourceHash If using `source`, this will force an update if the file content has updated but the filename has not.
         * 
         * @return builder
         * 
         */
        public Builder sourceHash(@Nullable Output<String> sourceHash) {
            $.sourceHash = sourceHash;
            return this;
        }

        /**
         * @param sourceHash If using `source`, this will force an update if the file content has updated but the filename has not.
         * 
         * @return builder
         * 
         */
        public Builder sourceHash(String sourceHash) {
            return sourceHash(Output.of(sourceHash));
        }

        public ContainerUploadArgs build() {
            $.file = Objects.requireNonNull($.file, "expected parameter 'file' to be non-null");
            return $;
        }
    }

}
